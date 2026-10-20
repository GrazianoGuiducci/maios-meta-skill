"""Exercise scoped freshness and pending work with two temporary repositories."""
import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from inspect_kernel_pair import git, main, repository_state


class InspectionTests(unittest.TestCase):
    def test_unrelated_commit_preserves_pending_port_and_missing_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            identities = []
            for name in ('source', 'receiver'):
                repo = workspace / name
                repo.mkdir()
                git(repo, 'init', '-q')
                (repo / 'kernel').mkdir()
                (repo / 'kernel/SKILL.md').write_text('Method A\n', encoding='utf-8')
                git(repo, 'add', '.')
                git(repo, '-c', 'user.name=Example', '-c', 'user.email=example@example.invalid', 'commit', '-qm', 'initial fixture')
                identities.append(dict(local_repo=name, assessed_repository_head=git(repo, 'rev-parse', 'HEAD'),
                    assessed_tree=git(repo, 'rev-parse', 'HEAD:kernel') if name == 'source' else git(repo, 'rev-parse', 'HEAD^{tree}')))
            identities[0]['root'] = 'kernel'
            source = workspace / 'source'
            (source / 'unrelated.txt').write_text('Outside the selected source tree\n', encoding='utf-8')
            git(source, 'add', '.')
            git(source, '-c', 'user.name=Example', '-c', 'user.email=example@example.invalid', 'commit', '-qm', 'unrelated change')
            state = repository_state(source, identities[0], 'kernel')
            self.assertTrue(state['repository_changed_since_assessment'])
            self.assertFalse(state['tree_changed_since_assessment'])
            self.assertIn('repository_only_drift', state)
            mapping = dict(schema='maios.neutral-kernel-port-map.v1', source=identities[0], destination=identities[1],
                owner_map=[dict(source_paths=['kernel/SKILL.md'], current_destination_paths=['missing.md'])],
                relation_states=[dict(id='pending', disposition='integrate', lifecycle='assessed_not_integrated', target_owner='receiver')],
                port_state='assessed_not_integrated')
            map_path = workspace / 'map.json'
            map_path.write_text(json.dumps(mapping), encoding='utf-8')
            stream = io.StringIO()
            with patch.object(sys, 'argv', ['inspect', '--workspace', str(workspace), '--map', str(map_path)]), contextlib.redirect_stdout(stream):
                self.assertEqual(main(), 0)
            report = json.loads(stream.getvalue())
            self.assertEqual(len(report['pending_relations']), 1)
            self.assertIn('continue pending', report['next_action'])
            self.assertEqual(report['mapped_path_coverage']['missing_current_destination_paths'], ['missing.md'])
            (source / 'kernel/SKILL.md').write_text('Changed method\n', encoding='utf-8')
            git(source, 'add', '.')
            git(source, '-c', 'user.name=Example', '-c', 'user.email=example@example.invalid', 'commit', '-qm', 'method change')
            self.assertTrue(repository_state(source, identities[0], 'kernel')['tree_changed_since_assessment'])


if __name__ == '__main__':
    unittest.main()

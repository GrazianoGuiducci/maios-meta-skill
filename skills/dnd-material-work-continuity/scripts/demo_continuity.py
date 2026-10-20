"""Create a small illustrative ledger in a new directory (Python 3.10+)."""
import argparse
import hashlib
import json
from pathlib import Path

from reduce_material_work_continuity import EVENT_SCHEMA, apply_event, initial_state, reconstruct


def run(output):
    output.mkdir(parents=True, exist_ok=False)
    state = initial_state('Example project', 'CURRENT_STATE.md', 'project owner')

    def save(name, value):
        (output / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    def event(event_id, kind, payload):
        nonlocal state
        item = dict(schema=EVENT_SCHEMA, event_id=event_id, event_kind=kind,
                    owner_surface=state['owner_surface'], previous_state_digest=state['state_digest'], payload=payload)
        save(event_id + '.event.json', item)
        state = apply_event(state, item)
        save(event_id + '.state.json', state)

    def source(event_id, text):
        event(event_id, 'source_event', dict(provenance_class='direct_operator', source_ref='inline:example',
              exact_text=text, source_digest=hashlib.sha256(text.encode('utf-8')).hexdigest(),
              secret_classified=False, source_gap_marker='', operative_status='active'))

    save('initial.state.json', state)
    source('S1', 'Prepare a draft for review. Do not publish it.')
    event('P1', 'assistant_projection', dict(projection='Prepare a public release now.', derives_from=['S1'], operative_status='active'))
    event('M1', 'verified_movement', dict(action_requested='prepare draft', action_performed='saved draft',
          evidence_refs=['illustrative:review-draft.md'], effects_observed=['draft-saved'],
          authority_before='project owner', authority_after='project owner'))
    source('S2', 'Correct the interpretation: the deliverable remains a draft for review.')
    event('R1', 'retraction_or_supersession', dict(retraction_authority_ref='S2', retracts=['P1'],
          scope='assistant interpretation', effective_relation_change='review draft, without publication',
          effects_not_reversed=['draft-saved']))
    event('C1', 'relation_checkpoint', dict(source_event_refs=['S1', 'S2'], projection_refs=[],
          current_relation='Draft saved; owner review remains the selected next movement.', unknowns=[],
          next_legal_action='read the saved draft with its owner', reopen_condition='new owner instruction or source change'))
    receipt = reconstruct(state)
    save('reconstruction.json', receipt)
    print(json.dumps({'directory': str(output), 'events': len(state['events']),
                      'state': receipt['finite_state'], 'effects_preserved': receipt['effects_preserved']}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True, help='New directory; existing directories are not overwritten.')
    run(parser.parse_args().output_dir)

import type { CollectionSummary } from '../lib/types'

type Props = {
  item: CollectionSummary
  selected: boolean
  onSelect: (item: CollectionSummary) => void
  onOpen: (item: CollectionSummary) => void
}

export function CollectionRow({ item, selected, onSelect, onOpen }: Props) {
  return (
    <div className="list-row" style={{ borderColor: selected ? '#1d4ed8' : undefined }}>
      <div>
        <strong>{item.name}</strong>
        <div className="muted">{item.display_id}</div>
      </div>
      <div style={{ display: 'flex', gap: '0.4rem' }}>
        <button onClick={() => onSelect(item)} type="button">Select</button>
        <button disabled={!item.has_subcollections} onClick={() => onOpen(item)} type="button">
          Open ›
        </button>
      </div>
    </div>
  )
}

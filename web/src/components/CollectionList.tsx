import type { CollectionSummary } from '../lib/types'
import { CollectionRow } from './CollectionRow'

type Props = {
  items: CollectionSummary[]
  selectedUri?: string
  onSelect: (item: CollectionSummary) => void
  onOpen: (item: CollectionSummary) => void
}

export function CollectionList({ items, selectedUri, onSelect, onOpen }: Props) {
  return (
    <div>
      {items.map((item) => (
        <CollectionRow
          key={item.uri}
          item={item}
          selected={item.uri === selectedUri}
          onOpen={onOpen}
          onSelect={onSelect}
        />
      ))}
    </div>
  )
}

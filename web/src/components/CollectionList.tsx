import type { CollectionNode } from "../lib/types";

type Props = {
  items: CollectionNode[];
  selectedUri: string | null;
  onSelect: (node: CollectionNode) => void;
  onOpen: (node: CollectionNode) => void;
};

export function CollectionList({ items, selectedUri, onSelect, onOpen }: Props) {
  return (
    <ul className="collection-list">
      {items.map((item) => (
        <li key={item.uri} className={selectedUri === item.uri ? "collection selected" : "collection"}>
          <button type="button" className="select-btn" onClick={() => onSelect(item)}>
            <div>{item.name}</div>
            <small>{item.storage_kind ?? "Storage"}</small>
          </button>
          <button
            type="button"
            className="open-btn"
            onClick={() => onOpen(item)}
            disabled={!item.has_subcollections}
            aria-label={`Open ${item.name}`}
          >
            Open ›
          </button>
        </li>
      ))}
    </ul>
  );
}

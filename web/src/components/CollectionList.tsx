import { CollectionNode } from "../lib/types";

interface Props {
  collections: CollectionNode[];
  selectedUri?: string;
  onSelect: (item: CollectionNode) => void;
  onOpen: (item: CollectionNode) => void;
}

export function CollectionList({ collections, selectedUri, onSelect, onOpen }: Props) {
  return (
    <ul style={{ listStyle: "none", padding: 0, margin: "1rem 0" }}>
      {collections.map((item) => {
        const selected = selectedUri === item.uri;
        return (
          <li
            key={item.uri}
            style={{
              border: "1px solid #ddd",
              borderRadius: 8,
              padding: 12,
              marginBottom: 8,
              background: selected ? "#eff6ff" : "white",
            }}
          >
            <button onClick={() => onSelect(item)} style={{ width: "100%", textAlign: "left", border: "none", background: "transparent" }}>
              <strong>{item.name}</strong>
              <div style={{ fontSize: 12, color: "#555" }}>{item.storage_kind}</div>
            </button>
            <button disabled={!item.has_subcollections} onClick={() => onOpen(item)} style={{ marginTop: 8 }}>
              Open ▶
            </button>
          </li>
        );
      })}
    </ul>
  );
}

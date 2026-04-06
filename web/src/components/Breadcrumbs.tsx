import { CollectionNode } from "../lib/types";

interface Props {
  items: CollectionNode[];
  onNavigate: (item: CollectionNode) => void;
}

export function Breadcrumbs({ items, onNavigate }: Props) {
  return (
    <nav aria-label="breadcrumb" style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
      {items.map((item, index) => (
        <button
          key={item.uri}
          onClick={() => onNavigate(item)}
          style={{
            border: "none",
            background: "transparent",
            color: "#0b5fff",
            textDecoration: "underline",
            cursor: "pointer",
          }}
        >
          {item.name}
          {index < items.length - 1 ? " /" : ""}
        </button>
      ))}
    </nav>
  );
}

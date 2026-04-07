import type { CollectionNode } from "../lib/types";

type Props = {
  trail: CollectionNode[];
  onNavigate: (index: number) => void;
};

export function Breadcrumbs({ trail, onNavigate }: Props) {
  return (
    <nav className="breadcrumbs" aria-label="collection breadcrumbs">
      {trail.map((node, index) => (
        <button key={node.uri} type="button" className="crumb" onClick={() => onNavigate(index)}>
          {index > 0 ? " / " : ""}
          {node.name}
        </button>
      ))}
    </nav>
  );
}

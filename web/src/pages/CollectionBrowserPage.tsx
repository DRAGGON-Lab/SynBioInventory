import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { Breadcrumbs } from "../components/Breadcrumbs";
import { CollectionList } from "../components/CollectionList";
import { MobileScaffold } from "../components/MobileScaffold";
import { api } from "../lib/api";
import type { CollectionNode } from "../lib/types";

export function CollectionBrowserPage() {
  const navigate = useNavigate();
  const [trail, setTrail] = useState<CollectionNode[]>([]);
  const [visible, setVisible] = useState<CollectionNode[]>([]);
  const [selected, setSelected] = useState<CollectionNode | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    void api
      .getRootCollections()
      .then((items) => setVisible(items))
      .catch((err) => setError((err as Error).message));
  }, []);

  async function openCollection(node: CollectionNode) {
    if (!node.has_subcollections) return;
    const children = await api.getSubcollections(node.uri);
    setTrail((prev) => [...prev, node]);
    setVisible(children);
    setSelected(null);
  }

  async function navigateTrail(index: number) {
    const nextTrail = trail.slice(0, index + 1);
    setTrail(nextTrail);
    const node = nextTrail[nextTrail.length - 1];
    const children = await api.getSubcollections(node.uri);
    setVisible(children);
    setSelected(null);
  }

  return (
    <MobileScaffold>
      <h2>Choose destination collection</h2>
      {trail.length > 0 && <Breadcrumbs trail={trail} onNavigate={navigateTrail} />}
      {error && <p className="error">{error}</p>}
      <CollectionList items={visible} selectedUri={selected?.uri ?? null} onSelect={setSelected} onOpen={openCollection} />
      <button
        type="button"
        disabled={!selected}
        onClick={() => {
          if (!selected) return;
          navigate("/create", { state: { destination: selected } });
        }}
      >
        Choose collection
      </button>
    </MobileScaffold>
  );
}

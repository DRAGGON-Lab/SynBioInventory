import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { Breadcrumbs } from "../components/Breadcrumbs";
import { CollectionList } from "../components/CollectionList";
import { MobileShell } from "../components/MobileShell";
import { api } from "../lib/api";
import { CollectionNode } from "../lib/types";

export function CollectionBrowserPage() {
  const navigate = useNavigate();
  const [stack, setStack] = useState<CollectionNode[]>([]);
  const [items, setItems] = useState<CollectionNode[]>([]);
  const [selected, setSelected] = useState<CollectionNode | null>(null);

  useEffect(() => {
    api.rootCollections().then((res) => setItems(res.items));
  }, []);

  async function openCollection(item: CollectionNode) {
    const res = await api.subcollections(item.uri);
    setStack((prev) => [...prev, item]);
    setItems(res.items);
    setSelected(null);
  }

  async function jumpTo(crumb: CollectionNode) {
    const index = stack.findIndex((entry) => entry.uri === crumb.uri);
    const nextStack = stack.slice(0, index + 1);
    const res = await api.subcollections(crumb.uri);
    setStack(nextStack);
    setItems(res.items);
    setSelected(crumb);
  }

  function choose() {
    if (!selected) return;
    sessionStorage.setItem("selected_collection", JSON.stringify(selected));
    navigate("/create");
  }

  return (
    <MobileShell>
      <h2>Choose destination collection</h2>
      <Breadcrumbs items={stack} onNavigate={jumpTo} />
      <CollectionList
        collections={items}
        selectedUri={selected?.uri}
        onSelect={(item) => setSelected(item)}
        onOpen={(item) => openCollection(item)}
      />
      <button onClick={choose} disabled={!selected}>Choose</button>
    </MobileShell>
  );
}

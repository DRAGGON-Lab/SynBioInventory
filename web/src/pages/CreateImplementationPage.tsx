import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

import { ImageUploader } from "../components/ImageUploader";
import { MobileScaffold } from "../components/MobileScaffold";
import { api } from "../lib/api";
import type { CollectionNode, InventoryType } from "../lib/types";

export function CreateImplementationPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const destination = (location.state as { destination?: CollectionNode } | null)?.destination;

  const [types, setTypes] = useState<InventoryType[]>([]);
  const [implementationType, setImplementationType] = useState("");
  const [name, setName] = useState("");
  const [builtUri, setBuiltUri] = useState("");
  const [barcode, setBarcode] = useState("");
  const [lotId, setLotId] = useState("");
  const [notes, setNotes] = useState("");
  const [images, setImages] = useState<File[]>([]);

  useEffect(() => {
    void api.getInventoryTypes().then((items) => {
      setTypes(items);
      if (items.length) setImplementationType(items[0].key);
    });
  }, []);

  if (!destination) {
    return (
      <MobileScaffold>
        <p>No destination selected.</p>
        <button onClick={() => navigate("/collections")}>Back to collections</button>
      </MobileScaffold>
    );
  }

  return (
    <MobileScaffold>
      <h2>Create implementation</h2>
      <p>Destination: {destination.name}</p>
      <div className="stack">
        <label>
          Implementation type
          <select value={implementationType} onChange={(e) => setImplementationType(e.target.value)}>
            {types.map((type) => (
              <option key={type.key} value={type.key}>
                {type.label}
              </option>
            ))}
          </select>
        </label>
        <label>
          Name (optional)
          <input value={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <label>
          Built URI (optional)
          <input value={builtUri} onChange={(e) => setBuiltUri(e.target.value)} />
        </label>
        <label>
          Barcode (optional)
          <input value={barcode} onChange={(e) => setBarcode(e.target.value)} />
        </label>
        <label>
          Lot ID (optional)
          <input value={lotId} onChange={(e) => setLotId(e.target.value)} />
        </label>
        <label>
          Notes (optional)
          <textarea value={notes} onChange={(e) => setNotes(e.target.value)} />
        </label>
      </div>
      <ImageUploader
        files={images}
        onAdd={(added) => setImages((prev) => [...prev, ...added])}
        onRemove={(index) => setImages((prev) => prev.filter((_, i) => i !== index))}
      />
      <button
        type="button"
        onClick={() =>
          navigate("/review", {
            state: {
              destination,
              implementationType,
              name,
              builtUri,
              barcode,
              lotId,
              notes,
              images,
            },
          })
        }
      >
        Continue to review
      </button>
    </MobileScaffold>
  );
}

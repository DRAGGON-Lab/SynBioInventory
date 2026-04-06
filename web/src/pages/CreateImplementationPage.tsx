import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { ImageUploader } from "../components/ImageUploader";
import { MobileShell } from "../components/MobileShell";
import { api } from "../lib/api";
import { CollectionNode, InventoryTypeOption } from "../lib/types";

export function CreateImplementationPage() {
  const navigate = useNavigate();
  const [types, setTypes] = useState<InventoryTypeOption[]>([]);
  const [selectedType, setSelectedType] = useState<string>("");
  const [name, setName] = useState("");
  const [notes, setNotes] = useState("");
  const [barcode, setBarcode] = useState("");
  const [lotId, setLotId] = useState("");
  const [builtUri, setBuiltUri] = useState("");
  const [images, setImages] = useState<File[]>([]);

  const selectedCollection = JSON.parse(sessionStorage.getItem("selected_collection") || "null") as CollectionNode | null;

  useEffect(() => {
    api.inventoryTypes().then(setTypes);
  }, []);

  function review() {
    if (!selectedCollection || !selectedType) return;
    const data = {
      destination_collection_uri: selectedCollection.uri,
      implementation_type: selectedType,
      name,
      notes,
      barcode,
      lot_id: lotId,
      built_uri: builtUri,
    };
    sessionStorage.setItem("create_payload", JSON.stringify(data));
    const transfer = new DataTransfer();
    images.forEach((img) => transfer.items.add(img));
    (window as Window & { __inventoryImages?: File[] }).__inventoryImages = Array.from(transfer.files);
    navigate("/review");
  }

  return (
    <MobileShell>
      <h2>Create inventory item</h2>
      <p>Destination: {selectedCollection?.name ?? "None selected"}</p>
      <label>
        Implementation type
        <select value={selectedType} onChange={(e) => setSelectedType(e.target.value)}>
          <option value="">Select type</option>
          {types.map((type) => (
            <option key={type.key} value={type.key}>{type.label}</option>
          ))}
        </select>
      </label>
      <label>Name<input value={name} onChange={(e) => setName(e.target.value)} /></label>
      <label>Notes<textarea value={notes} onChange={(e) => setNotes(e.target.value)} /></label>
      <label>Barcode<input value={barcode} onChange={(e) => setBarcode(e.target.value)} /></label>
      <label>Lot ID<input value={lotId} onChange={(e) => setLotId(e.target.value)} /></label>
      <label>Built URI<input value={builtUri} onChange={(e) => setBuiltUri(e.target.value)} /></label>
      <ImageUploader images={images} onChange={setImages} />
      <button onClick={review} disabled={!selectedType}>Review</button>
    </MobileShell>
  );
}

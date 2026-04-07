import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

import { MobileScaffold } from "../components/MobileScaffold";
import { api } from "../lib/api";
import type { CollectionNode } from "../lib/types";

type ReviewState = {
  destination: CollectionNode;
  implementationType: string;
  name?: string;
  builtUri?: string;
  barcode?: string;
  lotId?: string;
  notes?: string;
  images: File[];
};

export function ReviewSubmitPage() {
  const navigate = useNavigate();
  const { state } = useLocation();
  const review = (state as ReviewState | null) ?? null;
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  if (!review) {
    return (
      <MobileScaffold>
        <p>Nothing to review.</p>
        <button onClick={() => navigate("/collections")}>Start over</button>
      </MobileScaffold>
    );
  }

  async function submit() {
    if (!review) return;
    setSubmitting(true);
    setError(null);
    try {
      const response = await api.createInventory({
        destination_collection_uri: review.destination.uri,
        implementation_type: review.implementationType,
        name: review.name,
        built_uri: review.builtUri,
        barcode: review.barcode,
        lot_id: review.lotId,
        notes: review.notes,
        images: review.images,
      });
      navigate("/success", { state: response });
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <MobileScaffold>
      <h2>Review and submit</h2>
      <table>
        <tbody>
          <tr>
            <th>Collection</th>
            <td>{review.destination.name}</td>
          </tr>
          <tr>
            <th>Type</th>
            <td>{review.implementationType}</td>
          </tr>
          <tr>
            <th>Name</th>
            <td>{review.name || "(auto)"}</td>
          </tr>
          <tr>
            <th>Images</th>
            <td>{review.images.length}</td>
          </tr>
        </tbody>
      </table>
      {error && <p className="error">{error}</p>}
      <button disabled={submitting} onClick={submit}>
        {submitting ? "Submitting..." : "Submit"}
      </button>
    </MobileScaffold>
  );
}

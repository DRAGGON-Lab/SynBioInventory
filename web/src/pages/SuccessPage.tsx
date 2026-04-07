import { useLocation, useNavigate } from "react-router-dom";

import { MobileScaffold } from "../components/MobileScaffold";
import type { CreateInventoryResponse } from "../lib/types";

export function SuccessPage() {
  const navigate = useNavigate();
  const { state } = useLocation();
  const result = state as CreateInventoryResponse | null;

  if (!result) {
    return (
      <MobileScaffold>
        <p>No successful submission found.</p>
        <button onClick={() => navigate("/collections")}>Back to collections</button>
      </MobileScaffold>
    );
  }

  return (
    <MobileScaffold>
      <h2>Success</h2>
      <p>{result.message}</p>
      <p>
        Created URI: <code>{result.created_uri}</code>
      </p>
      <p>Attached images: {result.attached_images}</p>
      <button onClick={() => navigate("/collections")}>Create another</button>
    </MobileScaffold>
  );
}

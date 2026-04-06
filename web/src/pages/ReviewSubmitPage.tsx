import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { MobileShell } from "../components/MobileShell";
import { api } from "../lib/api";

export function ReviewSubmitPage() {
  const navigate = useNavigate();
  const [error, setError] = useState<string>();
  const payload = JSON.parse(sessionStorage.getItem("create_payload") || "{}");
  const images = (window as Window & { __inventoryImages?: File[] }).__inventoryImages ?? [];

  async function submit() {
    try {
      const response = await api.createInventory({ ...payload, images });
      sessionStorage.setItem("create_result", JSON.stringify(response));
      navigate("/success");
    } catch (err) {
      setError((err as Error).message);
    }
  }

  return (
    <MobileShell>
      <h2>Review submission</h2>
      <pre style={{ whiteSpace: "pre-wrap", wordBreak: "break-word" }}>{JSON.stringify(payload, null, 2)}</pre>
      <p>Images attached: {images.length}</p>
      <button onClick={submit}>Submit</button>
      {error ? <p style={{ color: "crimson" }}>{error}</p> : null}
    </MobileShell>
  );
}

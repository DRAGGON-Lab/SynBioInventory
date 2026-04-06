import { Link } from "react-router-dom";

import { MobileShell } from "../components/MobileShell";

export function SuccessPage() {
  const result = JSON.parse(sessionStorage.getItem("create_result") || "{}");

  return (
    <MobileShell>
      <h2>Inventory created</h2>
      <p>{result.message}</p>
      <p>
        Created URI: <code>{result.created_uri}</code>
      </p>
      <Link to="/collections">Create another</Link>
    </MobileShell>
  );
}

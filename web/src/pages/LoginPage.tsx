import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";

import { MobileScaffold } from "../components/MobileScaffold";
import { api } from "../lib/api";

export function LoginPage() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);
    try {
      const result = await api.login(username, password);
      if (result.authenticated) {
        navigate("/collections");
      }
    } catch (err) {
      setError((err as Error).message);
    }
  }

  return (
    <MobileScaffold>
      <h1>SynBioInventory</h1>
      <p>Sign in with your SynBioHub account.</p>
      <form onSubmit={handleSubmit} className="stack">
        <label>
          Username
          <input value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <label>
          Password
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        {error && <p className="error">{error}</p>}
        <button type="submit">Log in</button>
      </form>
    </MobileScaffold>
  );
}

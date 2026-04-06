import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";

import { MobileShell } from "../components/MobileShell";
import { api } from "../lib/api";

export function LoginPage() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string>();

  async function onSubmit(event: FormEvent) {
    event.preventDefault();
    try {
      await api.login(username, password);
      navigate("/collections");
    } catch (err) {
      setError((err as Error).message);
    }
  }

  return (
    <MobileShell>
      <h1>SynBioInventory</h1>
      <p>Login to SynBioHub</p>
      <form onSubmit={onSubmit} style={{ display: "grid", gap: 8 }}>
        <input value={username} placeholder="Username" onChange={(e) => setUsername(e.target.value)} required />
        <input type="password" value={password} placeholder="Password" onChange={(e) => setPassword(e.target.value)} required />
        <button type="submit">Login</button>
      </form>
      {error ? <p style={{ color: "crimson" }}>{error}</p> : null}
    </MobileShell>
  );
}

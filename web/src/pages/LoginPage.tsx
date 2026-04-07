import { FormEvent, useState } from 'react'
import { useNavigate } from 'react-router-dom'

import { Layout } from '../components/Layout'
import { login } from '../lib/api'

export function LoginPage() {
  const navigate = useNavigate()
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)

  async function onSubmit(event: FormEvent) {
    event.preventDefault()
    try {
      await login(username, password)
      navigate('/collections')
    } catch (err) {
      setError((err as Error).message)
    }
  }

  return (
    <Layout>
      <h1>SynBioInventory Login</h1>
      <form className="card" onSubmit={onSubmit}>
        <label>
          Username
          <input value={username} onChange={(e) => setUsername(e.target.value)} required />
        </label>
        <label>
          Password
          <input
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            type="password"
            required
          />
        </label>
        {error && <p style={{ color: '#b91c1c' }}>{error}</p>}
        <button type="submit">Sign in</button>
      </form>
    </Layout>
  )
}

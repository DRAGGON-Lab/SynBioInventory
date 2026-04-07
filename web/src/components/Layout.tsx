import { PropsWithChildren } from 'react'

export function Layout({ children }: PropsWithChildren) {
  return <main className="container">{children}</main>
}

import type { PropsWithChildren } from "react";

export function MobileScaffold({ children }: PropsWithChildren) {
  return (
    <div className="app-shell">
      <main className="app-card">{children}</main>
    </div>
  );
}

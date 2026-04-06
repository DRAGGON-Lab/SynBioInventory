import { PropsWithChildren } from "react";

export function MobileShell({ children }: PropsWithChildren) {
  return (
    <main
      style={{
        maxWidth: 760,
        margin: "0 auto",
        padding: "1rem",
        fontFamily: "system-ui, sans-serif",
      }}
    >
      {children}
    </main>
  );
}

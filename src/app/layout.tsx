import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "About Trender",
  description: "성수부터 전 세계 핫플까지, 당신만의 완벽한 여정을 그리세요. AI 기반 맞춤형 큐레이션 서비스 트렌더.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}

"use client";

import Image from "next/image";
import { useEffect, useState, useRef } from "react";

const KEYWORDS = [
  { text: "#성수동_핫플", color: "white", image: "/screen_hotplace.png" },
  { text: "#셀럽_추천코스", color: "white", image: "/screen_celeb.png" },
  { text: "#AI_큐레이션", color: "white", image: "/screen_ai.png" },
  { text: "#나만의_여정", color: "gold", image: "/screen_route.png" },
  { text: "#인스타그램_연동", color: "white", image: "/screen_instagram.png" },
  { text: "#친구와_함께", color: "white", image: "/screen_friends.png" },
  { text: "#점주님들도_쉽게", color: "white", image: "/screen_owner.png" },
];

export default function Home() {
  const [activeIndex, setActiveIndex] = useState(0);
  const [showTopBtn, setShowTopBtn] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleScroll = () => {
      if (containerRef.current) {
        const rect = containerRef.current.getBoundingClientRect();
        const sectionHeight = rect.height - window.innerHeight;
        const scrollPos = -rect.top;

        if (scrollPos < 0) {
          setActiveIndex(0);
        } else if (scrollPos > sectionHeight) {
          setActiveIndex(KEYWORDS.length - 1);
        } else {
          const index = Math.min(
            KEYWORDS.length - 1,
            Math.floor((scrollPos / sectionHeight) * KEYWORDS.length)
          );
          setActiveIndex(index);
        }
      }

      if (window.scrollY > 800) {
        setShowTopBtn(true);
      } else {
        setShowTopBtn(false);
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <div className="min-h-screen bg-[#050505] text-white selection:bg-gold selection:text-black font-sans">
      {/* Navigation */}
      <nav className="fixed top-0 z-50 flex w-full items-center justify-between px-4 md:px-8 py-4 md:py-6 glass-morphism">
        <div className="flex items-center">
          <Image
            src="/logo_full_new.png"
            alt="Trender Logo"
            width={150}
            height={40}
            className="h-8 md:h-9 w-auto invert"
          />
        </div>

        {/* Mobile Nav Actions */}
        <div className="flex md:hidden items-center gap-3">
          <a
            href="https://www.instagram.com/trendermap_official/"
            target="_blank"
            className="p-2 rounded-full bg-zinc-800 text-white"
          >
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.791-4-4s1.791-4 4-4 4 1.791 4 4-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
            </svg>
          </a>
          <a href="https://trender-fe.vercel.app/" target="_blank" className="rounded-full px-4 py-2 text-sm font-bold btn-shiny">체험하기</a>
        </div>

        {/* Desktop Nav */}
        <div className="hidden md:flex items-center gap-6 text-[15px] font-medium">
          <a href="#service" className="hover:text-gold transition-colors">Service</a>
          <a href="#features" className="hover:text-gold transition-colors">Features</a>
          <a
            href="https://www.instagram.com/trendermap_official/"
            target="_blank"
            className="rounded-full px-5 py-2 btn-insta flex items-center gap-2"
          >
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.791-4-4s1.791-4 4-4 4 1.791 4 4-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
            </svg>
            Instagram
          </a>
          <a href="https://trender-fe.vercel.app/" target="_blank" className="rounded-full px-6 py-2 transition-all font-bold btn-shiny">앱 체험하기</a>
        </div>
      </nav>

      {/* Hero Section with Central Logo */}
      <section className="relative flex min-h-screen flex-col items-center justify-center px-8 text-center overflow-hidden">
        <div className="animate-fade-in logo-center-container">
          <Image
            src="/logo_full.png"
            alt="Trender Full Logo"
            width={500}
            height={400}
            className="mb-8"
            priority
          />
          <div className="max-w-4xl">
            <h1 className="text-4xl font-extrabold leading-[1.3] md:text-6xl mb-6 px-4">
              <span className="gold-gradient">
                성수부터 전 세계 핫플까지, <br className="md:hidden" /> 당신만의 완벽한 여정을 그리세요.
              </span>
            </h1>
          </div>
        </div>
        <div className="absolute top-1/2 left-1/2 -z-10 h-[800px] w-[800px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-gold/5 blur-[150px]"></div>
      </section>

      {/* Split Keyword/Video Scroll Section */}
      <section ref={containerRef} className="keyword-container">
        <div className="keyword-split">
          <div className="keyword-list">
            {KEYWORDS.map((keyword, i) => (
              <span
                key={i}
                className={`keyword-item ${activeIndex === i ? "active" : ""} ${activeIndex === i && keyword.color === "gold" ? "gold" : ""}`}
              >
                {keyword.text}
              </span>
            ))}
          </div>

          <div className="keyword-video-fixed">
            <div className="device-frame">
              <div className="device-screen flex items-center justify-center bg-black">
                {KEYWORDS.map((keyword, i) => (
                  <Image
                    key={i}
                    src={keyword.image}
                    alt={keyword.text}
                    fill
                    className={`object-fill transition-opacity duration-500 ${activeIndex === i ? "opacity-100" : "opacity-0"}`}
                  />
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Description Section */}
      <section className="px-8 py-56 bg-zinc-950">
        <div className="mx-auto max-w-4xl text-center">
          <h2 className="text-3xl md:text-5xl font-bold leading-tight mb-16">
            평범한 이동을 <br className="md:hidden" />
            <span className="text-gold">특별한 경험</span>으로 디자인합니다.
          </h2>
          <div className="space-y-10 text-zinc-400 text-lg md:text-xl leading-relaxed max-w-3xl mx-auto">
            <p>
              트렌더(Trender)는 인스타그램 핫플레이스와 셀럽의 리얼 방문 데이터를 기반으로 <br className="hidden md:block" />
              당신의 취향에 딱 맞는 여정을 제안하는 전용 AI 큐레이터입니다.
            </p>
            <p>
              어렵게 검색할 필요 없습니다. 마음에 드는 곳을 슬롯에 담기만 하세요. <br className="hidden md:block" />
              나머지는 트렌더가 가장 효율적이고 감각적인 동선으로 연결해 드립니다.
            </p>
          </div>
        </div>
      </section>

      {/* Features Section - Clean Layout */}
      <section id="features" className="px-8 py-32 border-t border-white/5">
        <div className="mx-auto max-w-6xl">
          <div className="grid gap-8 md:grid-cols-3">
            {[
              {
                title: "감각적인 슬롯 편집",
                desc: "일정의 흐름을 한눈에 파악하고, 드래그 한 번으로 리듬감 있게 코스를 배치하세요.",
                icon: "🛤️"
              },
              {
                title: "취향 저격 AI 추천",
                desc: "피드에 저장하기만 했던 힙한 장소들을 AI가 엄선하여 최적의 타이밍에 제안합니다.",
                icon: "✨"
              },
              {
                title: "실시간 여정 공유",
                desc: "함께 가는 친구들과 실시간으로 아이디어를 나누며 우리만의 지도를 완성해 보세요.",
                icon: "🤝"
              }
            ].map((feature, i) => (
              <div key={i} className="bg-zinc-900/40 p-12 rounded-[2.5rem] border border-white/5 hover:border-gold/20 transition-all group text-center">
                <div className="text-5xl mb-8 group-hover:scale-110 transition-transform inline-block">{feature.icon}</div>
                <h3 className="text-2xl font-bold mb-4">{feature.title}</h3>
                <p className="text-zinc-500 leading-relaxed mx-auto max-w-[260px]">{feature.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Survey Section */}
      <section className="px-8 py-32 bg-zinc-950 flex justify-center">
        <div className="w-full max-w-4xl survey-card p-12 md:p-20 rounded-[3rem] text-center relative overflow-hidden">
          <div className="relative z-10 flex flex-col items-center">
            <h2 className="text-3xl md:text-5xl font-black mb-6">사용자 설문조사</h2>
            <p className="text-zinc-400 text-lg mb-12 leading-relaxed max-w-2xl">
              Trender 서비스 발전을 위해 여러분의 소중한 의견을 들려주세요.
            </p>
            <a
              href="https://bizcowork.co.kr/kanosurvey/171823"
              target="_blank"
              className="px-12 py-5 rounded-full survey-glow-button text-xl hover:scale-105 transition-transform"
            >
              설문 참여하기
            </a>
            <p className="mt-8 text-zinc-500 text-sm font-medium">
              설문조사 종료일: <span className="text-zinc-300">2026-08-21</span>
            </p>
          </div>
          <div className="absolute top-0 right-0 w-64 h-64 bg-white/5 blur-[80px] -translate-y-1/2 translate-x-1/2 rounded-full"></div>
        </div>
      </section>

      {/* Floating Top Button */}
      <button
        onClick={scrollToTop}
        className={`btn-top ${showTopBtn ? "visible" : ""}`}
        aria-label="Scroll to top"
      >
        <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 15l7-7 7 7" />
        </svg>
      </button>

      <footer className="border-t border-white/5 px-8 py-16 text-center text-zinc-600">
        <div className="flex items-center justify-center gap-2 mb-6">
          <Image src="/logo.png" alt="Logo" width={24} height={24} className="opacity-30 grayscale" />
          <span className="font-bold tracking-widest text-xs uppercase">Trender</span>
        </div>
        <p className="text-sm">© 2026 Trender. All rights reserved.</p>
      </footer>
    </div>
  );
}

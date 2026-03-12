"use client";

export default function CTA() {
  return (
    <section className="cta-section" id="contact">
      <div className="cta-section__bg">
        <img src="/images/cta.png" alt="Open road stretching into the sunset" />
      </div>
      <div className="cta-section__overlay" />
      <p className="section__label fade-up">Ready to Start?</p>
      <h2 className="cta-section__heading fade-up">
        Let&apos;s Move Your
        <br />
        Business <span className="accent">Forward</span>
      </h2>
      <a href="#" className="btn-primary fade-up">
        Get Started Today <span>&rarr;</span>
      </a>
    </section>
  );
}

import React from "react"

export default function HeroSection() {
    return (
        <section className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div className="container flex flex-col md:flex-row justify-center items-center mt-32 gap-10 md:gap-40">
                <div className="flex flex-col gap-4 md:order-1 order-2 w-full">
                    <h2 className="text-2xl md:text-5xl font-bold bg-clip-text text-transparent bg-black py-2">Summarization made simple with AI.</h2>
                    <p>Our AI-powered tools condense your text and video content into bite-sized summaries. Summarize your texts in just a few seconds</p>
                    <button className="w-1/2 rounded-lg font-medium text-lg p-2 bg-cyan-500 text-white">Get Started - it's free!</button>
                </div>
                <div className="flex rounded-lg p-4 bg-gray-500 shadow-lg border-2 border-black md:order-2 order-1">
                    <img src="https://cdn.pixabay.com/photo/2019/10/15/12/04/office-4551450_960_720.jpg" alt="books-computer" className="flex rounded-lg " />
                </div>
            </div>
        </section>
    )
}
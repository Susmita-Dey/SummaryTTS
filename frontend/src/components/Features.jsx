import React from 'react'
import FeatureCard from './FeatureCard'

export default function Features() {
    return (
        <section className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div className='container flex flex-col justify-center items-center'>
                <h2 className='text-4xl font-bold mt-24 text-center'>Features</h2>
                <div className='mt-16 flex flex-col md:flex-row gap-8'>
                    <FeatureCard />
                    <FeatureCard />
                    <FeatureCard />
                    <FeatureCard />
                </div>
            </div>
        </section>
    )
}

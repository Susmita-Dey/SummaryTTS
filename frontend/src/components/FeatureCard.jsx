import React from "react"
import { Card } from "flowbite-react"

export  default function FeatureCard() {
    return (
        <div className="max-w-sm">
            <Card
                imgAlt="Meaningful alt text for an image that is not purely decorative"
                imgSrc="https://flowbite.com/docs/images/blog/image-1.jpg"
            >
                <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                Summarize and Read Text Aloud
                </h5>
                <p className="font-normal text-gray-700 dark:text-gray-400">
                Summarize long articles and texts into shorter, more manageable summaries.
Customize the length of the summary to fit your needs.
Listen to the summary in a natural-sounding voice with text-to-speech technology.
                </p>
            </Card>
        </div>
    )
}


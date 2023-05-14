import React from 'react'
import { Footer } from 'flowbite-react'

export default function FooterComponent() {
    return (
        <footer className='mx-auto max-w-7xl px-2 sm:px-6 lg:px-8 mt-16 bg-white'>
            <Footer container={true} bgDark={true}>
                <div className="w-full text-center">
                    <div className="w-full justify-between sm:flex sm:items-center sm:justify-between">
                    </div>
                    <Footer.Divider />
                    <Footer.Copyright
                        href="#"
                        by="SummaryTTS™"
                        year={2023}
                    />
                </div>
            </Footer>
        </footer>
    )
}

import React from 'react'
import { Footer } from 'flowbite-react'

export default function FooterComponent() {
    return (
        <footer className='mx-auto max-w-7xl px-2 sm:px-6 lg:px-8 mt-16 bg-gray-900'>
            <Footer container={true} bgDark={true}>
                <div className="w-full text-center">
                    <div className="w-full justify-between sm:flex sm:items-center sm:justify-between">
                        <Footer.Brand
                            href="https://flowbite.com"
                            src="https://flowbite.com/docs/images/logo.svg"
                            alt="Flowbite Logo"
                            name="Flowbite"
                        />
                        <Footer.LinkGroup>
                            <Footer.Link href="#">
                                About
                            </Footer.Link>
                            <Footer.Link href="#">
                                Privacy Policy
                            </Footer.Link>
                            <Footer.Link href="#">
                                Licensing
                            </Footer.Link>
                            <Footer.Link href="#">
                                Contact
                            </Footer.Link>
                        </Footer.LinkGroup>
                    </div>
                    <Footer.Divider />
                    <Footer.Copyright
                        href="#"
                        by="Flowbite™"
                        year={2022}
                    />
                </div>
            </Footer>
        </footer>
    )
}

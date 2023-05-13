import React from 'react'
import "./auth_style.css"
import { auth, provider } from '../../config'
import { signInWithPopup } from 'firebase/auth'

export default function Authentication() {
    let Authenticated = false
    const signInWithGoogle = () => {
        signInWithPopup(auth, provider).then((result) => {
            localStorage.setItem("Authenticated", true)
            Authenticated = true
            window.location.pathname = "/"
            const email = result._tokenResponse.email
            localStorage.setItem("email", email)
            const name = result._tokenResponse.displayName
            localStorage.setItem("name", name)

        })
    }
    return (
        <div className='login'>
            <div className="image"></div>
            <div className="logincontent">
                <button onClick={signInWithGoogle} className="btn">Sign In With Google</button>
            </div>
        </div>
    )
}
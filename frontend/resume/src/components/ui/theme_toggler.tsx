import {Moon, Sun} from "lucide-react"
import {useEffect, useState} from "react"

export function ThemeToggler() {
    const [theme, setTheme] = useState<'light' | 'dark'>(() => {
        return (localStorage.getItem('theme') as 'light' | 'dark') ?? 'light'
    })

    useEffect(() => {
        document.documentElement.classList.toggle('dark', theme === 'dark')
        localStorage.setItem('theme', theme)
    }, [theme])

    return (
        <div
            className="fixed bottom-5 right-5 h-12 w-12 rounded-full flex items-center justify-center
                 bg-green-700 text-white cursor-pointer active:bg-green-700 active:scale-95"
            onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
        >
            {theme === 'light' ? <Moon/> : <Sun/>}
        </div>
    )
}

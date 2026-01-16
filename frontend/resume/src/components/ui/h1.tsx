import type {ReactNode} from "react";


interface TypographyH1Props {
    children: ReactNode;
    className?: string;
}

export function H1({children, className}: TypographyH1Props) {
    return (
        <h1 className={`scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance ${className ?? ""}`}>
            {children}
        </h1>
    )
}

import type {ReactNode} from "react";
import {cn} from "@/lib/utils.ts";

interface LargeTextProps {
    children?: ReactNode;
    className?: string;
}

export function LargeText(props: LargeTextProps) {
    return <div className={cn("text-lg font-semibold", props.className)}>{props.children}</div>
}
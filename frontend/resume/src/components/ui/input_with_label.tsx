import {Input} from "@/components/ui/input"
import {Label} from "@/components/ui/label.tsx";

interface InputWithLabelProps {
    label: string
    type?: string
    placeholder?: string
    id?: string
}

export function InputWithLabel({label, type = "text", id, placeholder = ""}: InputWithLabelProps) {

    id = id ?? label.toLowerCase().replaceAll(" ", "-")
    return (
        <div className="grid w-full items-center gap-3">
            <Label htmlFor={id}>{label}</Label>
            <Input type={type} id={id} placeholder={placeholder}/>
        </div>
    )
}

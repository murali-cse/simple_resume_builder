import {Select, SelectContent, SelectItem, SelectTrigger, SelectValue} from "@/components/ui/select.tsx";
import {Label} from "@radix-ui/react-label";

export function EndYear() {

    const currentYear: number = new Date().getFullYear()
    const years: number[] = Array.from({length: currentYear - 1950}, (_: unknown, i: number): number => currentYear - i)

    return <>
        <div className={"flex flex-col gap-2"}>
            <Label className={'text-sm font-medium'} htmlFor="end-year">End Year</Label>
            <Select>
                <SelectTrigger className="w-full">
                    <SelectValue placeholder="End Year"/>
                </SelectTrigger>
                <SelectContent className="popover">
                    {
                        ...years.map((val: number, index: number) => {
                            return <SelectItem key={index} value={`${val}`}>{val}</SelectItem>
                        })
                    }
                </SelectContent>
            </Select>
        </div>
    </>
}
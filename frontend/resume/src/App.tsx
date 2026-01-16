import {H1} from "@/components/ui/h1.tsx";
import {InputWithLabel} from "@/components/ui/input_with_label.tsx";
import {LargeText} from "@/components/ui/large.tsx";
import {StartYear} from "@/components/ui/start_year.tsx";
import {EndYear} from "@/components/ui/end_year.tsx";
import {Button} from "@/components/ui/button.tsx";
import {ThemeToggler} from "@/components/ui/theme_toggler.tsx";
import InputTags from "@/components/ui/input_tag.tsx";
import {Label} from "@radix-ui/react-label";


function App() {

    const testArr = Array.from({length: 1}, (_: unknown, i: number): string => `skill ${i}`)

    // useEffect(() => {
    //     const theme = localStorage.getItem('theme') ?? 'light'
    //
    //     if (theme === 'dark') {
    //         document.documentElement.classList.add("dark")
    //     } else {
    //         document.documentElement.classList.remove("dark")
    //     }
    // }, [])


    return <>
        <div className="min-h-screen flex justify-center relative">
            <ThemeToggler/>
            <div className="w-full lg:w-1/2 lg:min-w-1/2 py-10 px-5">
                <H1 className={"pb-10"}>Simple Resume Generator</H1>
                {/* Personal Details*/}
                <div className={"grid grid-cols-2 gap-5"}>
                    <div className={"col-span-2"}>
                        <LargeText>Personal Details</LargeText>
                    </div>
                    <div className={"col-start-1 col-end-3"}>
                        <InputWithLabel label={'Name'}/>
                    </div>
                    <InputWithLabel label={'Email'}/>
                    <InputWithLabel type={'number'} label={'Phone'}/>
                    <InputWithLabel label={'LinkedIn'}/>
                    <InputWithLabel label={'Github'}/>
                </div>
                {/* Education Details*/}
                <div className={"grid grid-cols-2 gap-5 pt-10"}>
                    <LargeText>Education Details</LargeText>
                    <div className={"w-full text-end"}>
                        <Button size={'sm'} className={"w-20 dark: bg-green-700 text-white"} onClick={() => {
                        }}>Add</Button>
                    </div>
                    <div className={"col-start-1 col-end-3"}>
                        <InputWithLabel label={'College Name'}/>
                    </div>
                    <StartYear/>
                    <EndYear/>
                    <InputWithLabel label={'Degree'}/>
                    <InputWithLabel label={'GPA'}/>
                </div>
                {/* Experience Details */}
                <div className={"grid grid-cols-2 gap-5 pt-10"}>
                    <LargeText>Experience Details</LargeText>
                    <div className={"w-full text-end"}>
                        <Button size={'sm'} className={"w-20 dark: bg-green-700 text-white"} onClick={() => {
                        }}>Add</Button>
                    </div>
                    <div className={"col-start-1 col-end-3"}>
                        <InputWithLabel label={'College Name'}/>
                    </div>
                    <StartYear/>
                    <EndYear/>
                    <InputWithLabel label={'Degree'}/>
                    <InputWithLabel label={'GPA'}/>
                </div>
                {/* Skills */}
                <div className={"grid grid-cols-2 gap-3 pt-10"}>
                    <LargeText className={'col-span-2'}>Skills</LargeText>
                    <div className={"col-span-2"}>
                        <Label className={'font-medium'}>Add your skills and separate it using comma</Label>
                        <InputTags className={"mt-2"} onChange={() => {
                        }} value={testArr} placeholder={'Enter skills'}/>
                    </div>
                </div>
                {/* Certifications */}
                <div className={"grid grid-cols-2 gap-3 pt-10"}>
                    <LargeText className={'col-span-2'}>Certifications</LargeText>
                    <div className={"col-span-2"}>
                        <Label className={'font-medium'}>Add your skills and separate it using comma</Label>
                        <InputTags onChange={() => {
                        }} value={['test', 'test2']} className={'col-span-2 mt-2'} placeholder={'Enter skills'}/>
                    </div>
                </div>
                {/* Projects */}
            </div>
        </div>

    </>
}

export default App;
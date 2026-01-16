import {H1} from "@/components/ui/h1.tsx";
import {InputWithLabel} from "@/components/ui/input_with_label.tsx";
import {LargeText} from "@/components/ui/large.tsx";
import {StartYear} from "@/components/ui/start_year.tsx";
import {EndYear} from "@/components/ui/end_year.tsx";
import {Button} from "@/components/ui/button.tsx";
import {ThemeToggler} from "@/components/ui/theme_toggler.tsx";
import InputTags from "@/components/ui/input_tag.tsx";
import {type SetStateAction, useState} from "react";
import {Label} from "@/components/ui/label.tsx";
import scribble from "./assets/scribble1.svg"


function App() {

    const [skills, setSkills] = useState<string[]>([])
    const [certifications, setCertifications] = useState<string[]>([])
    const [highlights, setHighlights] = useState<string[]>([])
    const [projectTech, setProjectTech] = useState<string[]>([])
    const [achievements, setAchievements] = useState<string[]>([])

    const updateAchievements = (val: SetStateAction<string[]>): void => {
        setAchievements(val)
    }
    const updateCertifications = (val: SetStateAction<string[]>): void => {
        setCertifications(val)
    }
    const updateHighlights = (val: SetStateAction<string[]>): void => {
        setHighlights(val)
    }
    const updateProjectTech = (val: SetStateAction<string[]>): void => {
        setProjectTech(val)
    }
    const updateSkills = (val: SetStateAction<string[]>): void => {
        setSkills(val)
    }


    return <>
        <div className="min-h-screen flex justify-center relative">
            <ThemeToggler/>
            <div className="w-full lg:w-1/2 lg:min-w-1/2 py-20 px-5">
                <div className={'flex flex-col items-center justify-center pb-10 gap-2'}>
                    <H1>Simple Resume Generator</H1>
                    <img src={scribble} alt="scribble" className={'w-1/2 h-7.5 mt-1'}/>
                </div>
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
                        <Button size={'sm'}
                                className={"w-20 dark: bg-green-700 active:bg-green-800 active:scale-95 text-white"}
                                onClick={() => {
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
                        <Button size={'sm'}
                                className={"w-20 dark: bg-green-700 active:scale-95 active:bg-green-800 text-white"}
                                onClick={() => {
                                }}>Add</Button>
                    </div>
                    <div className={"col-start-1 col-end-3"}>
                        <InputWithLabel label={'Company Name'}/>
                    </div>
                    <InputWithLabel label={'Role'}/>
                    <InputWithLabel label={'Location'}/>
                    <StartYear/>
                    <EndYear/>
                    <div className={"col-span-2"}>
                        <Label>Achievements (separate it using comma)</Label>
                        <InputTags onChange={updateAchievements} value={achievements}
                                   className={'col-span-2 mt-2'} placeholder={'Enter achievements'}/>
                    </div>
                </div>
                {/* Skills */}
                <div className={"grid grid-cols-2 gap-3 pt-10"}>
                    <LargeText className={'col-span-2'}>Skills</LargeText>
                    <div className={"col-span-2"}>
                        <Label>Add your skills and separate it using comma</Label>
                        <InputTags className={"mt-2"} onChange={updateSkills} value={skills}
                                   placeholder={'Enter skills'}/>
                    </div>
                </div>
                {/* Certifications */}
                <div className={"grid grid-cols-2 gap-3 pt-10"}>
                    <LargeText className={'col-span-2'}>Certifications</LargeText>
                    <div className={"col-span-2"}>
                        <Label>Add your Certificates and separate it using comma</Label>
                        <InputTags onChange={updateCertifications} value={certifications} className={'col-span-2 mt-2'}
                                   placeholder={'Enter your certifications...'}/>
                    </div>
                </div>
                {/* Projects */}
                <div className={"grid grid-cols-2 gap-5 pt-10"}>
                    <LargeText>Project Details</LargeText>
                    <div className={"w-full text-end"}>
                        <Button size={'sm'}
                                className={"w-20 bg-green-700 active:scale-95 active:bg-green-800 text-white"}
                                onClick={() => {
                                }}>Add</Button>
                    </div>
                    <div className={"col-start-1 col-end-3"}>
                        <InputWithLabel label={'Name'}/>
                    </div>
                    <div className={"col-span-2"}>
                        <Label>Add Technology Stacks (separate it using comma)</Label>
                        <InputTags onChange={updateProjectTech} value={projectTech} className={'col-span-2 mt-2'}
                                   placeholder={'Enter technology stacks'}/>
                    </div>
                    <div className={"col-span-2"}>
                        <Label>Highlights (separate it using comma)</Label>
                        <InputTags onChange={updateHighlights} value={highlights} className={'col-span-2 mt-2'}
                                   placeholder={'Enter project highlights'}/>
                    </div>
                    <div className={"col-span-2"}>
                        <div className={'grid grid-cols-2 gap-2'}>
                            <Label className={'text-sm font-medium col-span-2'}>Duration (optional)</Label>
                            <StartYear/>
                            <EndYear/>
                        </div>
                    </div>
                </div>
                <div className={'flex justify-center pt-10'}>
                    <Button className={'bg-green-700 active:bg-green-800 active:scale-95 text-white w-1/2 '} size={'lg'}
                            variant={'secondary'}>Generate</Button>
                </div>
            </div>
        </div>
    </>
}

export default App;
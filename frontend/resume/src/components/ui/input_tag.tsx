import type {ComponentProps, Dispatch, SetStateAction} from 'react'

import {cn} from '@/lib/utils'
import {X} from 'lucide-react'

const InputTags = ({
                       className,
                       onChange,
                       value: tags,
                       ...props
                   }: Omit<ComponentProps<'input'>, 'onChange' | 'value'> & {
    onChange: Dispatch<SetStateAction<string[]>>
    value: string[]
}) => (
    <label
        className={cn(
            'flex min-h-10 w-full cursor-text flex-wrap items-center gap-1 rounded-md border border-input bg-transparent p-1 text-sm transition-[color,box-shadow] disabled:cursor-not-allowed disabled:opacity-50 has-[input:focus-visible]:border-ring has-[input:focus-visible]:ring-[3px] has-[input:focus-visible]:ring-ring/50',
            className
        )}
    >
        {tags.map(t => (
            <span
                key={t}
                className="inline-flex items-center gap-1.5 rounded-md bg-zinc-600/10 px-2 py-1 text-sm font-medium text-zinc-700 dark:text-blue-400 transition-colors hover:bg-zinc-600/20 focus:ring-2 focus:ring-ring focus:ring-offset-1 focus:outline-none"
                tabIndex={0}
                role="button"
                aria-label={`Remove tag ${t}`}
                onKeyDown={e => {
                    if (e.key === 'Delete' || e.key === 'Backspace') {
                        e.preventDefault()
                        onChange(tags.filter(i => i !== t))
                    }
                }}
            >
        <span>{t}</span>
        <X
            className="size-3 cursor-pointer text-muted-foreground transition-colors hover:text-destructive"
            onClick={() => onChange(tags.filter(i => i !== t))}
            data-slot="icon"
        />
      </span>
        ))}
        <input
            className={cn(
                'ml-1 h-8 min-w-0 flex-1 appearance-none border-0 bg-transparent px-2 py-1 text-sm font-medium text-zinc-700 ring-0 transition-all duration-200 ease-out outline-none placeholder:text-zinc-500 placeholder:capitalize focus:outline-none dark:text-white',
                tags.length ? 'w-0 placeholder:opacity-0' : '', 'w-full'
            )}
            type="text"
            onKeyDown={e => {
                const {value} = e.currentTarget,
                    values = value
                        .split(/[,;]+/u)
                        .map(v => v.trim())
                        .filter(Boolean)
                if (values.length) {
                    if ([',', ';', 'Enter'].includes(e.key)) {
                        e.preventDefault()
                        onChange([...new Set([...tags, ...values])])
                        e.currentTarget.value = ''
                    }
                } else if (e.key === 'Backspace' && tags.length) {
                    e.preventDefault()
                    onChange(tags.slice(0, -1))
                }
            }}
            {...props}
        />
    </label>
)

export default InputTags

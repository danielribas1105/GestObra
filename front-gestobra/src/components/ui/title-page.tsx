"use client"
import { IconPlus } from "@tabler/icons-react"
import { Button } from "./button"
import Search from "./search"
import { Plus } from "lucide-react"

interface TitlePageProps {
	title: string
	subtitle?: string
	className?: string
	placeholder: string
	textButton: string
}

export default function TitlePage({ title, subtitle, className, placeholder, textButton }: TitlePageProps) {
	return (
		<div className={`${className ?? ""} flex justify-between items-center gap-20`}>
			<div className="flex flex-col justify-between">
				<h1 className="text-3xl text-logo-blue-dark font-logo font-bold">{title}</h1>
				<p className="mt-1 text-[16px] text-logo-blue-dark/70">{subtitle}</p>
			</div>
			<Search className="flex-1" placeholder={placeholder} />
			<Button className="flex gap-2">
				<IconPlus />
				<span>{textButton}</span>
			</Button>
		</div>
	)
}

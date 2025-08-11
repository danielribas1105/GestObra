import PageLayout from "@/components/ui/page-layout"
import TitlePage from "@/components/ui/title-page"

export default function SettingsPage() {
	return (
		<PageLayout>
			<section className="flex flex-col">
				<div className="flex flex-col justify-between">
					<h1 className="text-3xl text-logo-blue-dark font-logo font-bold">Configurações</h1>
					<p className="mt-1 text-[16px] text-logo-blue-dark/70">subtitle</p>
				</div>
			</section>
		</PageLayout>
	)
}

import PageLayout from "@/components/ui/page-layout"
import TitlePage from "@/components/ui/title-page"

export default function VehiclesPage() {
	return (
		<PageLayout>
			<section>
				<TitlePage
					title="Veículos"
					placeholder="Procure pela placa - Ex: oxk8978"
					textButton="Adicionar Veículo"
				/>
			</section>
		</PageLayout>
	)
}

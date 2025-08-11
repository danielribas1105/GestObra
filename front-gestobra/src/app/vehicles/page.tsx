import PageLayout from "@/components/ui/page-layout"
import TitlePage from "@/components/ui/title-page"
import ListVehicles from "@/components/vehicle/list-vehicles"

export default function VehiclesPage() {
	return (
		<PageLayout>
			<section className="flex flex-col gap-7">
				<TitlePage
					title="Veículos"
					placeholder="Procure pela placa - Ex: oxk8978"
					textButton="Adicionar Veículo"
				/>
				<div className="flex justify-center">
					<ListVehicles />
				</div>
			</section>
		</PageLayout>
	)
}

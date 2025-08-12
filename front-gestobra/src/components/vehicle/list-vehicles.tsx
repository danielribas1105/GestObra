import vehicles from "@/data/constants/Vehicles"
import VehicleCard from "./vehicle-card"

export default function ListVehicles() {
	return (
		<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
			{vehicles.map((vehicle) => (
				<VehicleCard key={vehicle.id} vehicle={vehicle} />
			))}
		</div>
	)
}

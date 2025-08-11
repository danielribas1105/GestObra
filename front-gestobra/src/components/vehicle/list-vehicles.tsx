import vehicles from "@/data/constants/Vehicles"
import CardVehicle from "./vehicle-card"

export default function ListVehicles() {
	return (
		<div className="grid grid-cols-4 gap-5">
			{vehicles.map((vehicle) => (
				<CardVehicle key={vehicle.id} vehicle={vehicle} />
			))}
		</div>
	)
}

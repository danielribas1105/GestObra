import Link from "next/link"
import Image from "next/image"
import { IconCircleFilled } from "@tabler/icons-react"
import Vehicle from "@/data/models/Vehicle"

export interface VehicleCardProps {
	vehicle: Vehicle
}

export default function VehicleCard({ vehicle }: VehicleCardProps) {
	return (
		<Link href={`/veiculos/${vehicle.id}`}>
			<article className="w-56 h-64 border-2 rounded-lg p-2 flex flex-col gap-2">
				<div className="relative w-full h-36 flex justify-center overflow-hidden">
					<Image
						src={vehicle.imagemURL}
						alt="Foto da veiculo"
						fill
						className="object-cover rounded-lg"
					/>
				</div>
				<div className="flex flex-col gap-1">
					<header>{vehicle.nome}</header>
					<section>Código: {vehicle.id}</section>
					<footer className="flex items-center gap-1">
						<IconCircleFilled size={16} color={vehicle.status === "ativo" ? "#00FF00" : "#FF0000"} />
						<span className="text-sm uppercase">{vehicle.status}</span>
					</footer>
				</div>
			</article>
		</Link>
	)
}

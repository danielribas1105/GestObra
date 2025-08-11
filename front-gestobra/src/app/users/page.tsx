import PageLayout from "@/components/ui/page-layout"
import TitlePage from "@/components/ui/title-page"

export default function UsersPage() {
	return (
		<PageLayout>
			<section className="flex flex-col">
				<TitlePage title="Usuários" placeholder="Procure pelo nome" textButton="Adicionar usuário" />
			</section>
		</PageLayout>
	)
}

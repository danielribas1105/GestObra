export default interface Vehicle {
	id: number
	nome: string
	placa: string
	ano_fabricacao: number
	km: number
	combustivel: string
	robustez: boolean
	capacidade_carga: string
	versatilidade: string
	status: "ativo" | "inativo"
	imagemURL: string
}

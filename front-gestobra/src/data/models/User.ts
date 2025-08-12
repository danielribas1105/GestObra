export default interface Vehicle {
	id: number
	nome: string
	cpf: string
	telefone: number
	status: "ativo" | "inativo"
	imagemURL: string
}

export default function UsePersistToken() {
	return (token: string) => {
		sessionStorage.setItem("token", token)
	}
}

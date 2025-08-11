import type { Metadata } from "next"
import { Geist, Geist_Mono, Tomorrow } from "next/font/google"
import "./globals.css"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/ui/app-sidebar"

const geistSans = Geist({
	variable: "--font-geist-sans",
	subsets: ["latin"],
})

const geistMono = Geist_Mono({
	variable: "--font-geist-mono",
	subsets: ["latin"],
})

const tomorrow = Tomorrow({
	weight: "500",
	style: "italic",
	subsets: ["latin"],
	variable: "--font-logo",
})

export const metadata: Metadata = {
	title: "GestObra",
	description: "Plataforma de gestão de obras e transporte de entulho",
}

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode
}>) {
	return (
		<html lang="pt-BR">
			<SidebarProvider>
				<AppSidebar />
				<body className={`${geistSans.variable} ${tomorrow.variable} antialiased`}>
					<SidebarTrigger />
					{children}
				</body>
			</SidebarProvider>
		</html>
	)
}

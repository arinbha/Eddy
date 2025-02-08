import Link from "next/link";

import { auth } from "~/server/auth";
import { api, HydrateClient } from "~/trpc/server";
import { UploadButton } from "./_components/upload";
import { redirect } from "next/navigation";

export default async function Home() {
  const hello = await api.post.hello({ text: "from tRPC" });
  const session = await auth();

  if (session?.user) {
    redirect("/home");
  }

  return (
    <HydrateClient>
      <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-b from-[#2e026d] to-[#15162c] text-white">
        <div className="container flex flex-col items-center justify-center gap-12 px-4 py-16">
          <div className="flex flex-col items-center gap-2">
            {!session && (
              <Link
                href="/api/auth/signin"
                className="rounded-full bg-white/10 px-10 py-3 font-semibold no-underline transition hover:bg-white/20"
              >
                Sign in
              </Link>
            )}
          </div>
        </div>
      </main>
    </HydrateClient>
  );
}

import Link from "next/link";
import { redirect } from "next/navigation";
import { Button } from "~/components/ui/button";
import { Input } from "~/components/ui/input";
import { auth } from "~/server/auth";
import { api, HydrateClient } from "~/trpc/server";
import { UploadButton } from "../_components/upload";

export default async function Home() {
  const session = await auth();
  const spaces = await api.room.search({ prefs: "study" });
  const schedule = await api.calendar.get();

  if (!session) {
    redirect("/");
  }

  return (
    <HydrateClient>
      <main className="flex h-screen flex-col bg-gradient-to-b from-[#2e026d] to-[#15162c] text-white">
        <header className="flex flex-row justify-between bg-gradient-to-b from-[#7148ab] to-[#15162c] p-4">
          <h1>Hello, {session.user.name}</h1>
          <div>
            <Link className="p-2" href="/group">
              Groups
            </Link>
            <Link className="p-2" href="/home">
              Settings
            </Link>
            <Link className="p-2" href="/api/auth/signout">
              Sign Out
            </Link>
          </div>
        </header>
        <div className="flex-rwo container flex h-full w-screen items-center justify-between px-4 py-16">
          <div>
            <div className="flex flex-row">
              <Input placeholder="Search spaces" />
              <Button type="submit">Search</Button>
            </div>
            <table>
              <tbody>
                {spaces?.map((val, idx) => <li key={idx}>{val}</li>)}
              </tbody>
            </table>
          </div>
          <div>
            {!schedule && <UploadButton />}
            {schedule && <div></div>}
          </div>
        </div>
        <footer className="flex flex-row justify-between bg-gradient-to-b from-[#7148ab] to-[#15162c] p-2">
          <p>Dummy notif</p>
        </footer>
      </main>
    </HydrateClient>
  );
}

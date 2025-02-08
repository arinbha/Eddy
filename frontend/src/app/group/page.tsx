"use client";

import Link from "next/link";
import { redirect } from "next/navigation";
import { Button } from "~/components/ui/button";
import { Input } from "~/components/ui/input";
import { useSession } from "next-auth/react";
import { useState } from "react";

export default function Home() {
  const { data: session, status } = useSession();
  const groups = [
    { name: "Group 1", id: 1 },
    { name: "Group 2", id: 2 },
    { name: "Group 3", id: 3 },
    { name: "Group 4", id: 4 },
    { name: "Group 5", id: 5 },
    { name: "Group 6", id: 6 },
  ];

  const [name, setName] = useState("");

  if (status === "unauthenticated") {
    redirect("/");
  }

  return (
      <main className="flex h-screen flex-col bg-gradient-to-b from-[#2e026d] to-[#15162c] text-white">
        <header className="flex flex-row justify-between bg-gradient-to-b from-[#7148ab] to-[#15162c] p-4">
          <h1>Hello, {session?.user.name}</h1>
          <div>
            <Link className="p-2" href="/group">
              Groups
            </Link>
            <Link className="p-2" href="/settings">
              Settings
            </Link>
            <Link className="p-2" href="/api/auth/signout">
              Sign Out
            </Link>
          </div>
        </header>
        <div className="flex-rwo container flex h-full w-screen items-center justify-between px-4 py-16">
          <table className="w-full">
            <thead className="text-center">
              <tr>
                <th>Name</th>
                <th>ID</th>
              </tr>
            </thead>
            <tbody>
              {groups.map((group) => (
                <tr key={group.id}>
                  <td>{group.name}</td>
                  <td>{group.id}</td>
                  <Button>Delete</Button>
                </tr>
              ))}
            </tbody>
          </table>
          <div>
            <div className="flex flex-row">
              <Input placeholder="Name" onChange={e => setName(e.target.value)}/>
              <Button>Create Group</Button>
            </div>

            <div className="flex flex-row">
              <Input placeholder="Name" />
              <Button>Join Group</Button>
            </div>
          </div>
        </div>
      </main>
  );
}
